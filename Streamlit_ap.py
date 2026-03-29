import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mobile Racing", layout="centered")

st.title("🏎️ Mobile Turbo Racer")
st.write("Touch LEFT or RIGHT side of the game to steer!")

# The Game Engine (HTML/JS)
game_html = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        body { margin: 0; background: #222; overflow: hidden; touch-action: none; display: flex; justify-content: center; }
        canvas { background: #333; width: 100vw; height: 70vh; max-width: 400px; border: 2px solid #555; }
    </style>
</head>
<body>
    <canvas id="g"></canvas>
    <script>
        const c = document.getElementById("g"), x = c.getContext("2d");
        let p = {x: 175, y: 480, w: 50, h: 80}, es = [], s = 0, gO = false, sp = 5;
        c.width = 400; c.height = 600;

        window.addEventListener('touchstart', e => {
            const t = e.touches[0].clientX, r = c.getBoundingClientRect();
            if ((t - r.left) * (400/r.width) < 200) p.x -= 50; else p.x += 50;
        });

        function frame() {
            if(gO) return;
            x.clearRect(0,0,400,600);
            x.fillStyle="white"; x.setLineDash([20,20]); x.beginPath(); x.moveTo(200,0); x.lineTo(200,600); x.stroke();
            
            p.x = Math.max(0, Math.min(350, p.x));
            x.fillStyle="#00D2FF"; x.fillRect(p.x, p.y, p.w, p.h);

            if(Math.random() < 0.02) es.push({x: Math.random()*350, y: -100});

            x.fillStyle="#FF4136";
            es.forEach((e, i) => {
                e.y += sp;
                x.fillRect(e.x, e.y, 50, 80);
                if(p.x < e.x+50 && p.x+50 > e.x && p.y < e.y+80 && p.y+80 > e.y) {
                    gO = true; alert("Score: " + s); location.reload();
                }
                if(e.y > 600) { es.splice(i,1); s++; sp += 0.1; }
            });
            x.fillStyle="white"; x.font="30px Arial"; x.fillText("Score: "+s, 20, 40);
            requestAnimationFrame(frame);
        }
        frame();
    </script>
</body>
</html>
"""

components.html(game_html, height=650)
