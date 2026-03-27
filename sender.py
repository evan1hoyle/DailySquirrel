<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Whimsical World of Chester Acornson</title>
    <style>
        :root {
            --forest-green: #4e6e5d;
            --berry-red: #b33939;
            --acorn-tan: #d2b48c;
            --magic-gold: #ffd700;
        }

        body {
            background-color: #fdfae6;
            background-image: radial-gradient(#e0dcc0 1px, transparent 1px);
            background-size: 20px 20px;
            color: #3d2b1f;
            font-family: 'Trebuchet MS', sans-serif;
            margin: 0;
            padding: 0;
            overflow-x: hidden;
        }

        /* Animated Floating Elements */
        .leaf {
            position: fixed;
            top: -50px;
            font-size: 24px;
            z-index: 10;
            animation: fall linear infinite;
            cursor: pointer; /* Now clickable! */
            user-select: none;
        }

        @keyframes fall {
            to { transform: translateY(110vh) rotate(360deg); }
        }

        header {
            text-align: center;
            padding: 3rem 1rem 1.5rem;
            background: linear-gradient(rgba(78, 110, 93, 0.15), transparent);
        }

        h1 {
            font-size: 2.2rem;
            margin: 0.5rem 0;
            color: var(--forest-green);
            text-shadow: 1px 1px #fff;
            transform: rotate(-1deg);
        }

        .wand-sparkle {
            color: var(--berry-red);
            font-weight: bold;
            font-size: 0.9rem;
            letter-spacing: 1px;
        }

        .main-content {
            max-width: 600px;
            margin: 0 auto;
            padding: 1rem;
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }

        .card {
            background: white;
            border: 3px dashed var(--acorn-tan);
            border-radius: 30px 10px 30px 10px;
            padding: 1.5rem;
            box-shadow: 5px 5px 0px var(--forest-green);
            transition: transform 0.2s ease;
        }

        .card:active {
            transform: scale(0.98);
        }

        h2, h3 {
            color: var(--forest-green);
            margin-top: 0;
            border-bottom: 2px dotted #eee;
            padding-bottom: 5px;
        }

        .backstory-text {
            line-height: 1.6;
            font-size: 0.95rem;
        }

        .badge-container {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 10px;
        }

        .stat-badge {
            background: var(--forest-green);
            color: white;
            padding: 6px 12px;
            border-radius: 15px;
            font-size: 0.8rem;
            white-space: nowrap;
        }

        .daily-list {
            padding-left: 1.2rem;
            line-height: 1.8;
        }

        footer {
            text-align: center;
            padding: 2rem;
            font-size: 0.75rem;
            color: #777;
        }

        .btn-squeak {
            background: var(--berry-red);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 50px;
            cursor: pointer;
            font-size: 1.1rem;
            width: 100%;
            font-weight: bold;
            box-shadow: 0 4px var(--acorn-tan);
            margin-bottom: 10px;
        }

        .btn-squeak:active {
            transform: translateY(3px);
            box-shadow: 0 1px var(--acorn-tan);
        }

        /* New Stash Style */
        .stash-counter {
            font-weight: bold;
            color: var(--berry-red);
        }
        
        #nap-status {
            font-size: 0.85rem;
            color: var(--forest-green);
            font-style: italic;
        }
    </style>
</head>
<body>

    <script>
        let nutCount = 0;

        function createLeaf() {
            const emojis = ['🍂', '🍃', '🍁', '🌰'];
            const leaf = document.createElement('div');
            leaf.className = 'leaf';
            leaf.style.left = Math.random() * 100 + 'vw';
            leaf.style.animationDuration = Math.random() * 3 + 4 + 's';
            leaf.style.opacity = Math.random() * 0.5 + 0.3;
            
            const emoji = emojis[Math.floor(Math.random() * emojis.length)];
            leaf.innerText = emoji;

            // Click functionality: Crunching leaves or collecting nuts
            leaf.onclick = () => {
                if (emoji === '🌰') {
                    nutCount++;
                    document.getElementById('nut-stash').innerText = nutCount;
                    leaf.innerText = '✨';
                    setTimeout(() => leaf.remove(), 200);
                } else {
                    leaf.innerText = '💥'; // "Crunch"
                    setTimeout(() => leaf.remove(), 150);
                }
            };

            document.body.appendChild(leaf);
            setTimeout(() => { if(leaf) leaf.remove() }, 7000);
        }
        
        setInterval(createLeaf, 800);

        // Nap Timer Logic
        function updateNapTimer() {
            const now = new Date();
            const napTime = new Date();
            napTime.setHours(14, 0, 0);

            let diff = napTime - now;
            const statusEl = document.getElementById('nap-status');

            if (diff > 0) {
                const mins = Math.floor((diff / 1000 / 60) % 60);
                const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
                statusEl.innerText = `Next nap in: ${hours}h ${mins}m`;
            } else if (now.getHours() === 14) {
                statusEl.innerText = "Current Status: 😴 Do not disturb.";
            } else {
                statusEl.innerText = "Nap concluded. Chester is hyper-active.";
            }
        }

        setInterval(updateNapTimer, 60000);
        window.onload = updateNapTimer;
    </script>

    <header>
        <span class="wand-sparkle">✦ TALES FROM THE HOLLOW ✦</span>
        <h1>Chester Acornson</h1>
        <p><em>Archivist of the Whispering Woods</em></p>
    </header>

    <main class="main-content">
        
        <section class="card">
            <h2>The Secret Origin</h2>
            <p class="backstory-text">
                Chester didn't just find his way into the woods; he was practically *summoned*. Legend says he discovered a forgotten library inside a hollowed-out Cedar and taught himself the ancient art of "Branch Navigation."
            </p>
            <p class="backstory-text">
                <strong>Current Stash:</strong> <span class="stash-counter" id="nut-stash">0</span> Acorns collected from the sky!
            </p>
        </section>

        <section class="card">
            <h3>Magical Skills</h3>
            <div class="badge-container">
                <span class="stat-badge">Telepathic Chattering</span>
                <span class="stat-badge">Moonlight Parkour</span>
                <span class="stat-badge">Nut Appraisal</span>
                <span class="stat-badge">Fluff Mastery</span>
            </div>
        </section>

        <section class="card">
            <h3>The Daily To-Do</h3>
            <ul class="daily-list" style="list-style-type: '🌰 '">
                <li>Polish the Silver Acorn</li>
                <li>Debate with a Grumpy Owl</li>
                <li>Organize leaves by "Crunch Level"</li>
                <li>14:00 - Mandatory Nap <br><span id="nap-status">Calculating naptime...</span></li>
            </ul>
        </section>
        
        <section class="card">
    <h3>Chester's Squirrel-fies</h3>
    <div class="selfie-gallery">
        
        <div class="polaroid" style="--r: -2deg;">
            <img src="YOUR_IMAGE_URL_1" alt="Chester posing with a nut">
            <div class="polaroid-caption">Feeling Nutty! 🌰</div>
        </div>

        <div class="polaroid" style="--r: 3deg;">
            <img src="YOUR_IMAGE_URL_2" alt="Chester in a sunbeam">
            <div class="polaroid-caption">Golden Hour ☀️</div>
        </div>

        <div class="polaroid" style="--r: -1deg;">
            <img src="YOUR_IMAGE_URL_3" alt="Chester's tail close up">
            <div class="polaroid-caption">Bad Fur Day? Never.</div>
        </div>

        <div class="polaroid" style="--r: 2deg;">
            <img src="YOUR_IMAGE_URL_4" alt="Chester meeting an owl">
            <div class="polaroid-caption">With Mr. Owl (He's grumpy)</div>
        </div>

    </div>
</section>

        <div style="padding: 0 10px;">
            <button class="btn-squeak" onclick="alert('Squeak! Chester is currently busy burying secrets. Check back later!')">
                SEND A SQUEAK
            </button>
            <p style="text-align: center; font-size: 0.8rem; opacity: 0.7;">Tip: Click the falling leaves to hear them "crunch" or catch acorns!</p>
        </div>

    </main>

    <footer>
        <p>© 2026 Whispering Woods Chronicles<br>Powered by 100% Organic Acorns<br>Stay bright and bushy-tailed!</p>
    </footer>

</body>
</html>