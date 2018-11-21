import logging
from travispy import TravisPy

t = TravisPy.github_auth('4f7dee0a7e00d04a575d3a338bba979264ccba10')
user = t.user()
repo = t.repo(user.login + '/travis-app')
build = t.build(repo.last_build_id)
state = build.check_state()
hooks = t.hooks()
logging.info('I told youdd so')