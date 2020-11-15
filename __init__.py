from git import Repo
import os


def get_inform_for_commit(repo, log):
    str_commit = str(log[-1])
    if len(log) == 1:
        index = str_commit.rfind('commit (initial):')\
                + len('commit (initial): ')
    else:
        index = str_commit.rfind('commit:') + len('commit: ')
    str_commit = str_commit[index:len(str_commit) - 1]
    write_info(repo, str_commit)


def write_info(repo, str_commit):
    if len(repo.tags) > 0:
        last_tag = sorted([i for i in repo.tags if i.tag is not None],
                          key=lambda t: t.tag.tagged_date)[-1]
        with open(path_to_version, 'w') as file:
            file.write(str(last_tag) + ' ')
    else:
        with open(path_to_version, 'w') as file:
            file.write('No version. ')
    with open(path_to_version, 'a') as file:
        file.write(str_commit)


def read_info_from_git():
    repo = Repo(os.getcwd())

    head = repo.head
    active_branch = head.reference

    log = active_branch.log()
    if not log:
        print(f'fatal: your current branch \'{active_branch}\''
              f'does not have any commits yet')
        exit(1)

    if not repo.index.diff(repo.head.commit):
        get_inform_for_commit(repo, log)
    else:
        get_inform_for_commit(repo, log)
        with open(path_to_version, 'a') as file:
            file.write(' You have changes to be committed')


path_to_version = os.path.split(__file__)[0] + '/VERSION'

if os.path.exists(os.getcwd() + '/.git'):
    if os.path.isfile(path_to_version):
        read_info_from_git()
    else:
        print(f'You deleted file VERSION from {path_to_version}.'
              f' It was not a good idea:( We cant do anything')
else:
    if os.stat(path_to_version).st_size == 0:
        print('No git. No any versions and commits of'
              'application.')
    else:
        print('No folder .git in your project.')


def show():
    if os.path.exists(path_to_version):
        with open(path_to_version, 'r') as f:
            return str(f.read())
    else:
        return "No information."

