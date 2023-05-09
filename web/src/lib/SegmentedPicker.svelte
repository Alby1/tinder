<script>
    import { setContext, onMount, createEventDispatcher } from "svelte";
    import { writable } from "svelte/store";

	const dispatch = createEventDispatcher();

    export let selectedIndex = 0;
    export const changeSelection = (index) => {
        console.log(selectedIndex, index);
        select(index);
    }

    let focusedSegmentIndex = writable(selectedIndex);
    let selectedSegmentIndex = writable(selectedIndex);
    let segments = [];
    let indexesIterator = -1;

    function select(segmentIndex) {
        if (segmentIndex >= 0 && segmentIndex < segments.length) {
            $focusedSegmentIndex = segmentIndex;

            if (!segments[segmentIndex].isDisabled) {
                $selectedSegmentIndex = $focusedSegmentIndex;
                dispatch('selectionchanged', {
                    index: $selectedSegmentIndex
                });
            }
        }
    }

    setContext("SegmentedPicker", {
        focusedSegmentIndex,
        selectedSegmentIndex,
        setIndex: () => {
            indexesIterator += 1;
            return indexesIterator;
        },
        addSegment: ({ index, isDisabled, length, offset }) => {
            if (index === $selectedSegmentIndex) {
                if (isDisabled) {
                    console.warn("Segmented Picker: avoid initially selecting a disabled segment.");
                }
            }
            segments = [...segments, { index, isDisabled, length, offset }]
        },
        setSelected: (segmentIndex) => {
            select(segmentIndex);
        }
    });

    onMount(() => {
        if (segments.length < 2) {
            console.warn("Segmented Picker: provide more than one element!");
        }
    });
</script>

<style>
    .segmented-picker {
        display: inline-flex;
        margin: 0;
        padding: 0.25rem;
        gap: 0.25rem;
        border-radius: 0.75rem;
        background-color: var(--accent);
    }
</style>

<div class="segmented-picker" {...$$restProps}>
    <slot/>
</div>