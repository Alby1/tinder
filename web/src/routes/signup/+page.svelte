<script>
	import SegmentedPicker from "../../lib/SegmentedPicker.svelte";
	import Segment from "../../lib/Segment.svelte";
	import InterestToggle from "../../lib/InterestToggle.svelte";

    let segmentedPickerChange;

    function segmentedPickerSelectionChanged(event) {
        const pages = document.querySelectorAll("[id^='segmented-page-']");
        pages.forEach(page => {
            page.style.display = "none";
        });
        const newPage = document.querySelector(`[id='segmented-page-${event.detail.index}']`);
        if (newPage) {
            newPage.style.display = "flex";
        }
    }

    function changeSegmentedPickerSelection(index) {
        segmentedPickerChange(index);
    }
</script>

<style>
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    form {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 0.25rem;
        margin-top: 1rem;
    }

    form > div {
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    input[type="text"],
    input[type="password"],
    input[type="email"] {
        width: 40ch;
    }

    button {
        width: 10ch;
    }

    .interests-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1rem;
    }
</style>

<title>Create your Tinder for Piffy&trade; account</title>
<div class="container" style="">
    <h2>Create your Tinder for Piffy&trade; account</h2>
    <SegmentedPicker id="segmented-picker" selectedIndex={0} bind:changeSelection={segmentedPickerChange} on:selectionchanged={(event) => { segmentedPickerSelectionChanged(event); }}>
        <Segment>Account Information</Segment>
        <Segment isClickable={false}>Your interests</Segment>
    </SegmentedPicker>
    <form id="segmented-page-0">
        <input type="email" id="emailText" placeholder="E-Mail Address">
        <input type="text" id="usernameText" placeholder="Username">
        <input type="password" id="passwordText" placeholder="Password">
        <div>
            <a href="/login">Log in</a>
            <button on:click={() => { changeSegmentedPickerSelection(1); }}>Next</button>
        </div>
    </form>
    <div id="segmented-page-1" style="display: none; flex-direction: column; align-items: center;">
        <h3>Choose your interests</h3>
        <div class="interests-grid">
            <InterestToggle image={"https://github.com/favicon.ico"} label={"test"}></InterestToggle>
            <InterestToggle image={"https://github.com/favicon.ico"} label={"test"}></InterestToggle>
            <InterestToggle image={"https://github.com/favicon.ico"} label={"test"}></InterestToggle>
            <InterestToggle image={"https://github.com/favicon.ico"} label={"test"}></InterestToggle>
            <InterestToggle image={"https://github.com/favicon.ico"} label={"test"}></InterestToggle>
            <InterestToggle image={"https://github.com/favicon.ico"} label={"test"}></InterestToggle>
            <InterestToggle image={"https://github.com/favicon.ico"} label={"test"}></InterestToggle>
            <InterestToggle image={"https://github.com/favicon.ico"} label={"test"}></InterestToggle>
        </div>
    </div>
</div>