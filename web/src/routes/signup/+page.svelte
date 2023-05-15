<script>
	import DottedProgress from "../../lib/DottedProgress.svelte";
    import Toggle from "../../lib/Toggle.svelte";
	import ToggleGroup from "../../lib/ToggleGroup.svelte";

    let dottedProgressChange;
    let selectedInterests = [];

    function dottedProgressSelectionChanged(event) {
        const pages = document.querySelectorAll("[id^='dotted-page-']");
        pages.forEach(page => {
            page.style.display = "none";
        });
        const newPage = document.querySelector(`[id='dotted-page-${event.detail.index}']`);
        if (newPage) {
            newPage.style.display = "flex";
        }
    }

    function changeDottedProgressSelection(index) {
        dottedProgressChange(index);
    }
</script>

<style>
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    [id^='dotted-page-'] {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 0.25rem;
        margin-top: 1rem;
    }

    [id^='dotted-page-'] > div {
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
<div class="container">
    <h2>Create your Tinder for Piffy&trade; account</h2>
    <DottedProgress count={2} bind:changeSelection={dottedProgressChange} on:selectionchanged={(event) => { dottedProgressSelectionChanged(event); }}/>
    <form id="dotted-page-0">
        <h3 style="align-self: center;">Account Information</h3>
        <label for="nameText">Name</label>
        <input type="text" id="nameText">
        <label for="surnameText">Surname</label>
        <input type="text" id="surnameText">
        <label for="birthDate">Date of birth</label>
        <input type="date" id="birthDate" style="width: 100%;">
        <label for="cityText">City</label>
        <select id="cityText" style="width: 100%;">
            <option value="city-1">City 1</option>
        </select>
        <label for="emailText">E-Mail Address</label>
        <input type="email" id="emailText">
        <label for="usernameText">Username</label>
        <input type="text" id="usernameText">
        <label for="passwordText">Password</label>
        <input type="password" id="passwordText">
        <div>
            <a href="/login">Log in</a>
            <button on:click={() => { changeDottedProgressSelection(1); }}>Next</button>
        </div>
    </form>
    <div id="dotted-page-1" style="display: none; flex-direction: column; align-items: center;">
        <h3>Choose your interests</h3>
        <ToggleGroup
            columns={4}
            on:selectedvalueadded={(event) => { selectedInterests.push(event.detail.addedValue); }}
            on:selectedvalueremoved={(event) => { selectedInterests.splice(selectedInterests.indexOf(event.detail.removedValue), 1); }}
            >
            <Toggle size={7} image={"https://www.donnad.it/sites/default/files/styles/r_visual_d/public/201940/collare-gatto-fai-da-te.jpg?itok=mY94HKXz"} label={"Animals"} value={0}/>
            <Toggle size={7} image={"https://cfx-wp-images.imgix.net/2017/11/DSC_0359.jpg?auto=compress%2Cformat&ixlib=php-3.3.0&s=ab2859378f945466c7393d28c535a97c"} label={"Cars"} value={1}/>
            <Toggle size={7} image={"https://academiabrasileiradeartes.org.br/wp-content/uploads/2021/05/tipos-de-arte-og.jpg"} label={"Arts"} value={2}/>
            <Toggle size={7} image={"https://staticg.sportskeeda.com/editor/2023/01/a319f-16742565001864-1920.jpg"} label={"Anime"} value={3}/>
            <Toggle size={7} image={"https://green-paths.com/wp-content/uploads/2021/05/Regalare-un-albero.png"} label={"Outdoors"} value={4}/>
            <Toggle size={7} image={"https://www.ibs.it/images/8716309087612_0_0_150_0_75.jpg"} label={"Videogames"} value={5}/>
            <Toggle size={7} image={"https://static.javatpoint.com/blog/images/advantages-and-disadvantages-of-information-technology2.jpg"} label={"Technology"} value={6}/>
            <Toggle size={7} image={"https://cdn.shopify.com/s/files/1/0005/1435/9356/files/01What_s_the_problem_with_travelling_and_film_photography_1024x1024.jpg?v=1655975765"} label={"Travelling"} value={7}/>
            <Toggle size={7} image={"https://cdn.britannica.com/25/193725-131-436D7C6C/sheet-music.jpg"} label={"Music"} value={8}/>
            <Toggle size={7} image={"https://im.hunt.in/cg/Jamalpur/City-Guide/eyelex.jpg"} label={"Cinema"} value={9}/>
            <Toggle size={7} image={"https://www.lifefitness.com/resource/image/1577926/portrait_ratio1x1/600/600/108d55725fc7dd0385f7176be6f523b2/aS/run-cx-treadmill-life-fitness-man-running-stride-edited-final-2000x1300.jpg"} label={"Fitness"} value={10}/>
        </ToggleGroup>
        <div>
            <button on:click={() => { changeDottedProgressSelection(0); }}>Back</button>
            <button>Next</button>
        </div>
    </div>
</div>