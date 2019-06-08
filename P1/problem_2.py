import os


def _find(suffix, path, results):
    
    if os.path.isdir(path):
        
        content = os.listdir(path)
        
        for descriptor in content:
            path_to_descriptor = os.path.join(path, descriptor)
            
            if os.path.isdir(path_to_descriptor):
                
                _find(suffix, path_to_descriptor, results)
                
            else:
                
                if suffix in path_to_descriptor:
                    results.append(path_to_descriptor)

                    
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    results = []
    _find(suffix, path, results)
    return results


def check(v):
    return "pass" if v is True else "failed"


def test_case(input_pattern, initial_directory, expected):

    print("--------------- TEST ---------------")
    result = sorted(find_files(input_pattern, initial_directory))
    ex = sorted(expected)
    print(check(result == ex), ":", result, ex)


test_case("", "", [])
test_case(".c", "./testdir", ['./testdir/subdir1/a.c', './testdir/t1.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c'])
test_case(".zip", "./testdir", ['./testdir/testdir.zip'])
test_case(".", "./testdir", ['./testdir/testdir.zip', './testdir/t1.h', './testdir/subdir1/a.c', './testdir/subdir1/a.h', './testdir/t1.c', './testdir/subdir2/.gitkeep', './testdir/subdir4/.gitkeep', './testdir/subdir3/subsubdir1/b.h', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/subdir5/a.h'])
# --------------- TEST ---------------
# pass : [] []
# --------------- TEST ---------------
# pass : ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c'] ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']
# --------------- TEST ---------------
# pass : ['./testdir/testdir.zip'] ['./testdir/testdir.zip']
# --------------- TEST ---------------
# pass : ['./testdir/subdir1/a.c', './testdir/subdir1/a.h', './testdir/subdir2/.gitkeep', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir3/subsubdir1/b.h', './testdir/subdir4/.gitkeep', './testdir/subdir5/a.c', './testdir/subdir5/a.h', './testdir/t1.c', './testdir/t1.h', './testdir/testdir.zip'] ['./testdir/subdir1/a.c', './testdir/subdir1/a.h', './testdir/subdir2/.gitkeep', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir3/subsubdir1/b.h', './testdir/subdir4/.gitkeep', './testdir/subdir5/a.c', './testdir/subdir5/a.h', './testdir/t1.c', './testdir/t1.h', './testdir/testdir.zip']
