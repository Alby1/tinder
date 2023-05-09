<!-- Logic -->
<script>
    import { page } from "$app/stores";

    let pages = [
        {"pageName": "Home", "pageUrl": "/"},
        {"pageName": "About", "pageUrl": "/about"}
    ];

    $: selectedPage = $page.url.pathname;
</script>

<!-- Style -->
<style>
    nav {
        position: fixed;
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

    nav a {
        padding: 1rem;
        text-decoration: none;
        transition: .25s ease;
        color: whitesmoke;
    }

    nav:hover a:not(:hover) {
        color: var(--darker-accent);
    }

    nav:hover a:hover,
    nav a[selected="true"] {
        color: white;
    }
    
    nav:hover a:hover {
        box-shadow: 0 2px 0 0 var(--lighter-accent);
    }
    
    nav a[selected="true"] {
        box-shadow: 0 2px 0 0 var(--darker-accent);
        font-weight: 500;
    }

    nav > div {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
</style>

<!-- HTML -->
<nav>
    <div>
        <h2 style="margin: 0;">Tinder for Piffy</h2>
        {#each pages as page}
            <a href="{page.pageUrl}" selected={selectedPage == page.pageUrl ? "true" : "false"}>{page.pageName}</a>
        {/each}
    </div>
    <div>
        <a href="/login" selected={selectedPage == "/login" ? "true" : "false"}>Login</a>
    </div>
</nav>