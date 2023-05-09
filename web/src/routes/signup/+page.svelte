<script>
	import Navbar from "../../lib/Navbar.svelte";
	import SegmentedPicker from "../../lib/SegmentedPicker.svelte";

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

    input[type="submit"] {
        width: 20ch;
    }
</style>

<div class="container" style="">
    <h2>Create your Tinder for Piffy&trade; account</h2>
    <SegmentedPicker elements={["Account information", "Your interests"]} pages={[Navbar, Navbar]}></SegmentedPicker>
    <form onsubmit="event.preventDefault();">
        <input type="email" id="emailText" placeholder="E-Mail Address">
        <input type="text" id="usernameText" placeholder="Username">
        <input type="password" id="passwordText" placeholder="Password">
        <div>
            <a href="/signup">Log in</a>
            <input type="submit" value="Create account">
        </div>
    </form>
</div>