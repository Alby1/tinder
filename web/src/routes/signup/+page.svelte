<script>
	import SegmentedPicker from "../../lib/SegmentedPicker.svelte";
	import Segment from "../../lib/Segment.svelte";
	import Toggle from "../../lib/Toggle.svelte";
	import ToggleGroup from "../../lib/ToggleGroup.svelte";

    let segmentedPickerChange;
    let selectedInterests = [];

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

    function selectedInterestsChanged(event) {

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
        <ToggleGroup columns={4} on:selectedChanged={(event) => { selectedInterestsChanged(event); }}>
            <Toggle image={"https://www.donnad.it/sites/default/files/styles/r_visual_d/public/201940/collare-gatto-fai-da-te.jpg?itok=mY94HKXz"} label={"Animals"}></Toggle>
            <Toggle image={"https://cfx-wp-images.imgix.net/2017/11/DSC_0359.jpg?auto=compress%2Cformat&ixlib=php-3.3.0&s=ab2859378f945466c7393d28c535a97c"} label={"Cars"}></Toggle>
            <Toggle image={"https://academiabrasileiradeartes.org.br/wp-content/uploads/2021/05/tipos-de-arte-og.jpg"} label={"Arts"}></Toggle>
            <Toggle image={"https://staticg.sportskeeda.com/editor/2023/01/a319f-16742565001864-1920.jpg"} label={"Anime"}></Toggle>
            <Toggle image={"https://green-paths.com/wp-content/uploads/2021/05/Regalare-un-albero.png"} label={"Outdoors"}></Toggle>
            <Toggle image={"https://www.ibs.it/images/8716309087612_0_0_150_0_75.jpg"} label={"Videogames"}></Toggle>
            <Toggle image={"https://static.javatpoint.com/blog/images/advantages-and-disadvantages-of-information-technology2.jpg"} label={"Technology"}></Toggle>
            <Toggle image={"https://cdn.shopify.com/s/files/1/0005/1435/9356/files/01What_s_the_problem_with_travelling_and_film_photography_1024x1024.jpg?v=1655975765"} label={"Travelling"}></Toggle>
            <Toggle image={"https://cdn.britannica.com/25/193725-131-436D7C6C/sheet-music.jpg"} label={"Music"}></Toggle>
            <Toggle image={"https://im.hunt.in/cg/Jamalpur/City-Guide/eyelex.jpg"} label={"Cinema"}></Toggle>
            <Toggle image={"https://www.lifefitness.com/resource/image/1577926/portrait_ratio1x1/600/600/108d55725fc7dd0385f7176be6f523b2/aS/run-cx-treadmill-life-fitness-man-running-stride-edited-final-2000x1300.jpg"} label={"Fitness"}></Toggle>
        </ToggleGroup>
    </div>
</div>