{
  singers{
    edges{
      node{
        id
        Name
        Email
      }
    }
  }
}
# ======================
{
  "data": {
    "singers": {
      "edges": [
        {
          "node": {
            "id": "U2luZ2VyVHlwZTox",
            "Name": "gagan",
            "Email": "gaggarwal124@gmail.com"
          }
        },
        {
          "node": {
            "id": "U2luZ2VyVHlwZToy",
            "Name": "neha",
            "Email": "neha@neha.com"
          }
        },
        {
          "node": {
            "id": "U2luZ2VyVHlwZToz",
            "Name": "rohit",
            "Email": "Rohit@gmail.com"
          }
        },
        {
          "node": {
            "id": "U2luZ2VyVHlwZTo0",
            "Name": "puja",
            "Email": "puja@gmail.com"
          }
        }
      ]
    }
  }
}
# ===========create singer
mutation {
  createSinger(Name:"Sunit", Phone:"765765", Email: "sunikrr@gmail.com"){
    singer{
      Name
      Phone
      Email
    }
  }
}
# =========update singer
mutation {
  updateSinger(id: 2, Name: "roshni", Phone: "42322", Email: "roshni@gmail.com") {
    singer {
      id
      Name
      Email
      Phone
    }
  }
}
# ============delete singer
mutation{
  deleteSinger(id:2){
    singer{
      Name
    }
  }
}
