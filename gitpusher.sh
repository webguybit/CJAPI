read -p "Commit description: " desc
git pull origin main
git add -A &&\
git commit -m "$desc" &&\
git push origin main