<!-- Logic -->
<script>
    import { page } from "$app/stores";

    let pages = [
        {"pageName": "Home", "pageUrl": "/"},
        {"pageName": "About", "pageUrl": "/about"}
    ];

    $: selectedPage = $page.url.pathname;

    function toggleProfileMenu() {
        const profileMenu = document.querySelector("#profileMenu");
        if (profileMenu.style.display == "flex") {
            profileMenu.style.display = "none";
        } else {
            profileMenu.style.display = "flex";
        }
    }
</script>

<!-- Style -->
<style>
    nav {
        position: sticky;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-inline: 0.5rem;
        top: 0;
        left: 0;
        right: 0;
        background-color: var(--accent);
        gap: 1rem;
    }

    nav .navbar-link {
        padding: 1rem;
        text-decoration: none;
        transition: .25s ease;
        color: black;
    }

    nav:hover .navbar-link:not(:hover) {
        color: var(--darker-accent);
    }

    nav:hover .navbar-link:hover,
    nav .navbar-link[selected="true"] {
        color: black;
    }
    
    nav:hover .navbar-link:hover {
        box-shadow: 0 2px 0 0 var(--lighter-accent);
    }
    
    nav .navbar-link[selected="true"] {
        box-shadow: 0 2px 0 0 var(--darker-accent);
        font-weight: 500;
    }

    nav > div {
        display: flex;
        align-items: center;
        gap: 1rem;
    }

    #profileMenuHolder {
        position: relative;
    }

    #profileMenu {
        width: 20ch;
        display: none;
        flex-direction: column;
        gap: 1rem;
        overflow: hidden;
        background-color: var(--accent);
        padding: 1rem;
        position: absolute;
        right: 0;
        top: 3.2rem;
    }

    .profile-link {
        color: unset;
    }
</style>

<!-- HTML -->
<nav>
    <div>
        <h2 style="margin: 0;">Tinder for Piffy&trade;</h2>
        {#each pages as page}
            <a href="{page.pageUrl}" selected={selectedPage == page.pageUrl ? "true" : "false"} class="navbar-link">{page.pageName}</a>
        {/each}
    </div>
    <div id="profileMenuHolder">
        <button on:click={toggleProfileMenu} style="all: unset; padding: 0.5rem !important; cursor: pointer !important;" class="navbar-link">
            <img src="/icons/user.svg" alt="Your profile icon" style="height: 2rem;"/>
        </button>
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <div id="profileMenu" on:click={toggleProfileMenu}>
            <a href="/profile" class="profile-link">Your profile</a>
            <a href="/login" class="profile-link">Login</a>
        </div>
    </div>
</nav>