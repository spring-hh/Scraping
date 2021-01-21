from bs4 import BeautifulSoup
import requests
import tkinter as tk

git_version = ""
git_flag = False
git_lb = ""

node_version = ""
node_flag = False
node_lb = ""

def return_git_version():
    global git_flag, git_version, git_lb
    if git_flag is False:
        html = requests.get('https://git-scm.com')
        soup = BeautifulSoup(html.text, 'lxml')
        git_version = soup.findAll('span', {'class': 'version'})
        git_version = git_version[0].text
        git_lb = tk.Label(text=git_version)
        git_lb.pack()
        git_flag = True
    else:
        git_lb.pack_forget()
        git_flag = False

def return_node_version():
    global node_flag, node_version, node_lb
    if node_flag is False:
        html = requests.get('https://nodejs.org/ja/')
        soup = BeautifulSoup(html.text, 'lxml')
        node_version = soup.findAll('a', {'class': 'home-downloadbutton'})
        node_version = node_version[0].text.splitlines()[1]
        node_lb = tk.Label(text=node_version)
        node_lb.pack()
        node_flag = True
    else:
        node_lb.pack_forget()
        node_flag = False

root = tk.Tk()
root.title("ツールバージョン")
root.geometry("450x350")

#widget
git_bt = tk.Button(text="git", command=return_git_version)
git_bt.pack()

git_bt = tk.Button(text="node", command=return_node_version)
git_bt.pack()

root.mainloop()