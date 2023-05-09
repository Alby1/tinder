<script>
    import "../global.css";
    import * as env from '$env/static/public';
	import Navbar from "../lib/Navbar.svelte";
</script>
<div style="--accent:{env.PUBLIC_ACCENT_COLOR}; --lighter-accent:{env.PUBLIC_LIGHTER_ACCENT_COLOR}; --darker-accent:{env.PUBLIC_DARKER_ACCENT_COLOR};">
    <Navbar></Navbar>
    <main>
        <slot/>
    </main>
</div>