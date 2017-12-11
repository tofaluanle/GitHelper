import json


class GitBean:
    def __init__(self):
        self.uri = "123"
        self.name = "123"
        self.branch = "123"
        self.path = "123"

    def __str__(self) -> str:
        # return "no: " + str(self.no) + ", path: " + self.path + ", md5: " + self.md5
        return json.dumps(self, default=lambda obj: obj.__dict__)

    @staticmethod
    def parse(json):
        git = GitBean()
        git.uri = json['uri']
        git.name = json['name']
        git.branch = json['branch']
        git.path = json['path']
        return git


# p1 = PatchBean()
# print(p1.md5)
# p1.md5 = "321"
# print(p1.md5)
# p1.no = 3
# p2 = PatchBean()
# p2.no = 1
# p3 = PatchBean()
# p3.no = 2
# list = [p1, p2, p3]
# for git in list:
#     print(git)
# list.sort(key=lambda git: git.no)
# for git in list:
#     print(git)
#
# print("========")
# if len(list) > 0:
#     list.sort(key=lambda git: git.no)
#
# while len(list) > 0:
#     list.remove(list[len(list) - 1])
#
# for git in list:
#     print(git)