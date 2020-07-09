#SIMPLE BRUTE FORCE FOR CISCO MD5#

python main.py "your hash" "your sal"

for exemple :
$1$iUjJ$VBEych385cM3HzyQY3KpL.

--that $1 represents encryption
--separate with $
--iUjJ represents salt
-- VBEych385cM3HzyQY3KpL. is the footprint


use :
python main.py '$1$iUjJ$VBEych385cM3HzyQY3KpL.' iUjJ
