<script>
    export let elements;
    export let pages;

    $: currentIndex = 0;

    function handleSelection(index) {
        currentIndex = index;
    }
</script>

<style>
    .segmented {
        display: flex;
        flex-direction: column;
    }
    
    .items {
        width: 100%;
        background-color: var(--lighter-accent);
        border-radius: 0.75rem;
        display: flex;
        gap: 1rem;
        padding: 0.5rem;
    }

    .items > div {
        font-size: smaller;
        background-color: var(--accent);
        padding: 0.5rem;
        border-radius: 0.5rem;
        cursor: pointer;
    }
</style>

<div class="segmented">
    <div class="items">
        {#each elements as element, i}
            <div on:click={() => {handleSelection(i)}}>{element}</div>
        {/each}
    </div>
    <div class="currentPage">
        <svelte:component this={pages[currentIndex]}/>
    </div>
</div>