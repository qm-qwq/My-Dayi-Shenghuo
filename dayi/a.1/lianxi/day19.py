# import os
# path = os.path.join('folder','subfolder','file.txt')
# print(os.path.exists(path))
#
# from pathlib import Path
# path = Path('folder')/'subfolder'/'file.txt'
# print(path.exists())

# from pathlib import Path
# p = Path('.')
# print(p.resolve())
#
# home = Path.home()
# config = home/'.config'/'app'/'settings.json'
# print(config)
#
# config = home.joinpath('.config','app','settings.json')
# print(config)

# p = Path('new_folder')
# p.mkdir(exist_ok=True)
# p2 = Path('parent/child/gtandchild')
# p2.mkdir(parents=True,exist_ok=True)
# p2.rmdir()
# print(p2)
# from pathlib import Path
# for child in Path('.').iterdir():
#     print(child)
#
#
# # for f in Path('.').glob('*.txt'):
# #     print(f)
#
# for f in Path('.').glob('*.py'):
#     print(f)





from pathlib import Path
from sys import path

from lianxi.main import count

n = input("输入路径").strip()
if not n:
    path = Path.cwd()
else:
    path = Path(n)

p = list(path.rglob("*.py"))
print(f"找到{len(p)}个文件")
for i,p in enumerate(p,1):
    print(f"{i}.{p.resolve()}")









