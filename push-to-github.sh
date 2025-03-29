#!/bin/bash

cd ~/JetsonNano  # Vaihda tähän sun projektikansio

echo "📦 Lisää muutokset..."
git add .

# Tee kommit-viestiksi nykyinen päivä ja aika
msg="päivitys: $(date '+%Y-%m-%d %H:%M:%S')"

echo "📝 Commitoidaan: $msg"
git commit -m "$msg"

echo "🚀 Pusketaan GitHubiin..."
git push

echo "✅ Valmis!"
