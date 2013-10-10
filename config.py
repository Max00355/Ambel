import landerdb
import protect
import getpass

data = {

        "blog_title":"Frankie's Blog",
        "blog_description":"",
        "admin":"frankie",
        "name":"Frankie",
        "db":"ambel.db",
        "debug":True,

}


if __name__ == "__main__":
    db = landerdb.Connect(data['db'])
    db.insert("admin", {"username":data['admin'], "password":protect.protect(getpass.getpass("Admin Password: ")), "name":data['name']})
    db.insert("posts", {})
    db.remove("posts", {})
