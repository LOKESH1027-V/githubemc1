class tr:
    def __init__(self,name,courese,pages):
        self.name=name
        self.courese=courese
        self.pages=pages
    def __str__(self):#dunder or magical methods
        return f"Hi i am {self.name} and my course is {self.courese}"
    def __len__(self):
        return self.pages
    def __call__(self, *args, **kwargs):
        return "HI"
d=tr("loki","python",300)
print(d)
print(len(d))
print(d())