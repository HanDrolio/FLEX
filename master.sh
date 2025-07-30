#!/bin/bash
echo "🧠 Booting ULTIMA.RUN: Hacker Artcore Mode..."
sleep 1
python3 mainframe_ui.py &
python3 broadcast_sync.py &
python3 mentalsync.py &
echo "🔋 All systems go. Mythic signal cast. 🌌"
