<script>
    import { setContext, onMount, createEventDispatcher } from "svelte";

	const dispatch = createEventDispatcher();

    export let count = 1;
    export let selectedIndex = 0;
    export const changeSelection = (index) => {
        select(index);
    }
    
    $: sIndex = selectedIndex;
    
    let items = [...Array(count).keys()];
    let indexesIterator = -1;

    function select(index) {
        if (index >= 0 && index < count) {
            selectedIndex = index;
            dispatch('selectionchanged', {
                index: selectedIndex
            });
        }
    }

    setContext("DottedProgress", {
        setIndex: () => {
            indexesIterator += 1;
            return indexesIterator;
        },
        setSelected: (segmentIndex) => {
            select(segmentIndex);
        }
    });

    onMount(() => {
        if (count < 2) {
            console.warn("Dotted Progress: provide more than one element!");
        }
    });
</script>

<style>
    .dotted-progress {
        display: flex;
        margin: 0;
        padding: 0.25rem;
        gap: 0.25rem;
        background-color: transparent;
    }

    .dotted-progress-item {
        width: 0.5rem;
        aspect-ratio: 1;
        border-radius: 100%;
    }
</style>

<div class="dotted-progress">
    {#each items as item}
        <div class="dotted-progress-item" style="background-color: {item == sIndex ? "var(--accent)" : item < sIndex ? "var(--darker-accent)" : "white"}; border: 1px solid {item == sIndex ? "var(--accent)" : item < sIndex ? "var(--darker-accent)" : "black"};"></div>
    {/each}
</div>