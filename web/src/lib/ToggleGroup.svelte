<script>
    import { setContext, onMount } from "svelte";

    let selectedElements = [];
    let toggles = [];

    export let columns = 4;

    setContext("ToggleGroup", {
        addSelected: (element) => {
            selectedElements.push(element);
        },
        removeSelected: (element) => {
            selectedElements.splice(selectedElements.indexOf(element), 1);
        },
        addToggle: (toggle) => {
            toggles = [...toggles, toggle];
        }
    });

    onMount(() => {
        if (toggles.length < 2) {
            console.warn("ToggleGroup: provide more than one element!");
        }
    });
</script>

<style>
    .container {
        display: grid;
        gap: 1rem;
    }
</style>

<div class="container" style="grid-template-columns: repeat({columns}, 1fr);">
    <slot/>
</div>