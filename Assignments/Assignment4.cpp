#include<bits/stdc++.h>
#define int long long
#define l long
#define mk make_pair
#define pb push_back
#define in insert
#define se second
#define fi first
#define mod 1000000007
#define watch(x) cout << (#x) << " is " << (x) << "\n"
#define fast ios_base::sync_with_stdio(false); cin.tie(NULL);
#define pii pair<int,int>
using namespace std;
vector<int> v[100005];
int par[100005],dis[100005],low[100005], num = 0,total,ev=0,n,si[100005];
bool vi[100005];
void numberofnodes(int s, int e)
{
    si[s] = 1;
    vi[s] = true;
    for (auto u : v[s])
    {
        if(vi[u]) continue;
        numberofnodes(u, s);
        si[s] += si[u];
    }
}
void dfs(int so)
{
	vi[so] = true;
	static int tit = 0;
	dis[so] = low[so] = ++tit;
    num++;
	for(auto u: v[so])
	{
		if(!vi[u])
		{
			par[u] = so;
            dfs(u);
			low[so] = min(low[so],low[u]);
			if(low[u]>dis[so])
			{
	            int bi = so,bo = u;
	            //if(bo<bi) swap(bi,bo);
                if(si[u]!=0 and (n-si[u])!=0) total++;
                if(si[u]%2==0 and (n-si[u])%2==0) ev++;
			} 		

		}
		else if(u!=par[so])
		{
			low[so] = min(low[so],dis[u]);
		}
	}
}
int modInverse(int a, int m) 
{ 
    int m0 = m; 
    int y = 0, x = 1; 
  
    if (m == 1) 
      return 0; 
  
    while (a > 1) 
    { 
        int q = a / m; 
        int t = m; 

        m = a % m, a = t; 
        t = y; 
        y = x - q * y; 
        x = t; 
    } 
    if (x < 0) 
       x += m0; 
  
    return x; 
} 
signed main()
{
    fast;
    #ifndef ONLINE_JUDGE
	freopen("input.txt","r", stdin);
    freopen("output.txt","w",stdout);
    #endif
	int m,i;
	cin>>n>>m;
	for(i=0;i<m;i++)
	{
		int a,b;
		cin>>a>>b;
        v[a].pb(b);
        v[b].pb(a);
	}
    
	memset(par,-1,sizeof(par));
    numberofnodes(1,0);
    memset(vi,false,sizeof vi);
    dfs(1);
    //for(i=1;i<=n;i++) watch(si[i]);
    int q = modInverse(total,mod);
    int p1 = (ev%mod * q)%mod;
    int p2 = (1 - p1 + mod)%mod;
    if(total==0) cout<<"0"<<" "<<"0";
    else cout<<p1<<" "<<p2;
}