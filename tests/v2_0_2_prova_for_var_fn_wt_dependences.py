import queue
import pickle
from AkitaCode.document import Document
# Create a database instance.
# import config_mod
q = queue.Queue()
# db = config_mod.get_db_path()
db = "C:/Users/aamat/.akitacan/data.db"
# Get path of file.
filename = "(v.2.0.2)_prova_var_fn_inside_for_statement_wt_depencences"
in_filename = "E:/Akitacan/dev/test/{}{}".format(filename,".atd")
out_filename = "E:/Akitacan/dev/test/{}{}".format(filename,".akita")

# Create a document instance.
doc = Document(in_filename, db)

# print(doc._error)
# print(doc._error_msg) if doc._error_msg is not None else print("Success!!")

fase_A = doc.check_syntax(q)
print("FASE A: {}".format(fase_A))
print(q.get())
if fase_A:
    fase_B = doc.check_spell(q)
    print("FASE B: {}".format(fase_B))
    print(q.get())
    if fase_B:
        fase_C = doc.makec(q,out_filename,autoclose=True)
        print("FASE C: {}".format(fase_C))
        while True:
            msg = q.get()
            if msg == True:
                break
            if fase_C == 0:
                f = pickle.load(open(out_filename,"rb"))
                f = f["data"]
            print(msg)