<!-- Logic -->
<script>
    import * as env from '$env/static/public';

    let pages = [
        {"pageName": "Home", "pageUrl": "/"},
        {"pageName": "About", "pageUrl": "/about"}
    ];

    export let selectedPage;
</script>

<!-- Style -->
<style>
    nav {
        position: fixed;
        display: flex;
        align-items: center;
        padding-inline: 0.5rem;
        top: 0;
        left: 0;
        right: 0;
        background-color: var(--accent);
        gap: 1rem;
    }

    nav > a {
        padding: 1rem;
        text-decoration: none;
        transition: .25s ease;
        color: whitesmoke;
    }

    nav:hover > a:not(:hover) {
        color: var(--darker-accent);
    }

    nav:hover > a:hover,
    nav > a[selected="true"] {
        color: white;
    }
    
    nav:hover > a:hover {
        box-shadow: 0 2px 0 0 var(--lighter-accent);
    }
    
    nav > a[selected="true"] {
        box-shadow: 0 2px 0 0 var(--darker-accent);
        font-weight: 500;
    }
</style>

<!-- HTML -->
<nav style="--accent:{env.PUBLIC_ACCENT_COLOR}; --lighter-accent:{env.PUBLIC_LIGHTER_ACCENT_COLOR}; --darker-accent:{env.PUBLIC_DARKER_ACCENT_COLOR};">
    <h2 style="margin: 0;">Tinder for Piffy</h2>
    {#each pages as page}
        <a href="{page.pageUrl}" selected={selectedPage == page.pageName ? "true" : "false"}>{page.pageName}</a>
    {/each}
</nav>