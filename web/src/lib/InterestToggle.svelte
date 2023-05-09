<script>
    
    export let label;
    export let image;

    $: isChecked = false;
</script>

<style>
    button {
        position: relative;
        width: 6rem;
        aspect-ratio: 1;
        background-color: transparent;
        border: 1px solid black;
        background-repeat: no-repeat;
        background-size: cover;
        border-radius: 1rem;
    }
    
    button[aria-checked="true"]::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: black;
        opacity: 0.2;
        border-radius: 1rem;
    }
    
    button > div {
        position: absolute;
        left: 0;
        bottom: 0;
        width: 100%;
        border-radius: 0 0 1rem 1rem;
        padding-block: 0.2rem;
    }
</style>

<button style="background-image: url({image});"
    role="checkbox"
    aria-checked={isChecked}
    on:click
    on:click|preventDefault={() => {
        isChecked = !isChecked;
    }}>
    <div style="background-color: {isChecked ? 'black' : 'white'}; color: {isChecked ? 'white' : 'black'}">{label}</div>
</button>