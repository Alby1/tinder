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
    }

    form > div {
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    input[type="text"],
    input[type="password"] {
        width: 40ch;
    }

    input[type="submit"] {
        width: 20ch;
    }
</style>

<title>Log in to your Tinder for Piffy&trade; account</title>
<div class="container" style="">
    <h2>Log in to your Tinder for Piffy&trade; account</h2>
    <form onsubmit="event.preventDefault();">
        <input type="text" id="usernameText" placeholder="Username or E-Mail address">
        <input type="password" id="passwordText" placeholder="Password">
        <div>
            <a href="/signup">Create an account</a>
            <input type="submit" value="Log in">
        </div>
    </form>
</div>