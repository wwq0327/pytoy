from fabric.api import run, env, local, prompt

env.hosts = ['joinwee.com']
env.user = 'wyatt'

def hello():
    local("pwd")
    local("ls -lh")
    

def remote():
    run("pwd")
    run("ls")
