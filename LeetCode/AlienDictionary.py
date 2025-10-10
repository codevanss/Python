class Solution:
    def alienOrder(self, words):
        adj = {c: set() for w in words for c in w}

        for i in range(len(words)-1):
            w1 ,w2 = words[i] , words[i+1]
            minLen = min(len(w1) , len(w2))
            if len(w1) > len(w2) and w1[ : minLen] == w2[ : minLen]:
                return ""
            
        visit = {}
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)
        
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)