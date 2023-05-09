<script>
    import { getContext, onMount } from "svelte";

    export let label = 'Label';
    export let isDisabled = false;
    export let isClickable = true;

    let ref = null;
    let length = 0;
    let offset = 0;

    const context = getContext("SegmentedPicker");
    const index = context.setIndex();
    const focusedSegmentIndex = context.focusedSegmentIndex;
    const selectedSegmentIndex = context.selectedSegmentIndex;

    $: isFocused = $focusedSegmentIndex === index;
    $: if (isFocused) { ref?.focus(); }
    $: isSelected = $selectedSegmentIndex === index;

    onMount(() => {
        context.addSegment({ index, isDisabled, length, offset });
    });
</script>

<style>
    .segmented-picker-item {
        margin: 0;
        padding: 0.5rem;
        border: none;
        border-radius: 0.5rem;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        transition: background-color 275ms;
        background-color: transparent;
        cursor: pointer;
    }

    .segmented-picker-item[aria-selected="true"] {
        background-color: var(--lighter-accent);
        cursor: default;
    }

    .segmented-picker-item[aria-disabled="true"] {
        opacity: 0.5;
        cursor: not-allowed;
    }
</style>

<button bind:this={ref}
    class="segmented-picker-item"
    role="tab"
    aria-selected={isSelected}
    aria-disabled={isDisabled}
    tabIndex={isSelected ? '0' : '-1'}
    {...$$restProps}
    on:click
    on:click|preventDefault={() => {
        if (index !== $selectedSegmentIndex && !isDisabled && isClickable) {
            context.setSelected(index);
        }
    }}>
    <slot>{label}</slot>
</button>