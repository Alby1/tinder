<script>
    import { setContext, onMount, createEventDispatcher } from "svelte";

    const dispatch = createEventDispatcher();

    let selectedValues = [];
    let toggles = [];

    export let columns = 4;

    setContext("ToggleGroup", {
        addSelected: (newValue) => {
            selectedValues.push(newValue);
            dispatch('selectedvalueschanged', {
                values: selectedValues
            });
            dispatch('selectedvalueadded', {
                addedValue: newValue
            });
        },
        removeSelected: (oldValue) => {
            selectedValues.splice(selectedValues.indexOf(oldValue), 1);
            dispatch('selectedvalueschanged', {
                values: selectedValues
            });
            dispatch('selectedvalueremoved', {
                removedValue: oldValue
            });
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