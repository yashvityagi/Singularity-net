from hyperon import MeTTa, G, ValueAtom, V, GroundedAtom, E
import os

metta = MeTTa()
#metta.run('''
   #(= (extractGenere $genre $space)
    #(match $space ($id $title $genre $actor $year $dir $des) ($id $title $genre $actor $year $dir $des)))
    #(= (ex))
#''')
# path = "./data.metta"
result=[]
with open("data.metta") as file:
    metta.run(file.read())
    result = metta.run('''! (extractGenere "Drama" &self)''')
    for r in result[0]:
        print(r)
# print(len(result[0]))
    

user_input=str(input("enter genre:"))
# gounded_atom = GroundedAtom(v)
# if os.path.exists("test.metta"):
#     with open("test.metta", "r") as f:
#         file_contents = f.read()
#         metta = MeTTa()
#     metta.run(file_contents)
# r = metta.run('!(extractGenere gounded_atom &self)')
pattern = E(V('id'), V('title'), ValueAtom(user_input), V('actor'), V('yr'), V('dir'), V('disc'))
obj = metta.space().query(pattern)
for o in obj:
    print(o)
    # result = metta.evaluate_atom(extractGenere gounded_atom &self)
# print(r)
# else:
#     print("File 'test.metta' not found.")