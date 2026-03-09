class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]

        path=path.split('/')
        print(path)
        for dir in path:
            if dir=='.' or dir=='':
                continue
            elif dir !='..':
                stack.append(dir)
            else:
                if stack:
                    stack.pop()
        return ('/'+'/'.join(stack))

        