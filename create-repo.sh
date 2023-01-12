#/bin/sh

REPOSITORY_PATH="repo"

RICK="Pickle Rick<Pickle.Rick@company.com>"
NUTS="Nuts Peanut<Nuts.Peanut@company.com>"
DUCKY="Ducky Duck<Ducky.Duck@company.com>"

rm -rf $REPOSITORY_PATH
mkdir $REPOSITORY_PATH
cd $REPOSITORY_PATH
git init

# 1st commit
README="README.md"
touch $README
git add .
git commit -m "Empty Readme added" --author="$RICK"

# Feature A
echo 'Feature A' > "feature-a.txt"
git add .
git commit -m "Add Feature A" --author="$NUTS"

# Feature B
echo 'Feature B' > "feature-b.txt"
git add .
git commit -m "Add Feature B" --author="$RICK"

# Feature C
echo 'Feature C' > "feature-c.txt"
git add .
git commit -m "Add Feature C" --author="$NUTS"

# Fix Feature A
echo 'Feature A (FIXED)' > "feature-a.txt"
rm -rf  "feature-b.txt"
git add .
git commit -m "Fix Feature A" --author="$DUCKY"

# Feature D
echo 'Feature D' > "feature-d.txt"
git add .
git commit -m "Add Feature D" --author="$RICK"

# Feature E
echo 'Feature E' > "feature-e.txt"
git add .
git commit -m "Add Feature E" --author="$NUTS"
