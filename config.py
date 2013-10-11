import landerdb
import protect
import getpass

data = {

        "blog_title":"Inqre Dev Blog",
        "blog_description":"",
        "admin":"inqre",
        "name":"Inqre Team",
        "debug":False,
        "db":"ambel.db",

}


if __name__ == "__main__":
    db = landerdb.Connect(data['db'])
    db.insert("admin", {"username":data['admin'], "password":protect.protect(getpass.getpass("Admin Password: ")), "name":data['name']})
    db.insert("posts", {})
    db.remove("posts", {})
