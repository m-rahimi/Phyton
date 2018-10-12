from multiprocessing import Pool

def apply_func_on_series(data=None, func=None, key=None):
    return data.apply(lambda x: func(x, key=key))


def multi_apply_func_on_series(df=None, func=None, key=None, n_jobs=4):
    p = Pool(n_jobs)
    f_ = p.map(functools.partial(apply_func_on_series, func=func, key=key),
               np.array_split(df, n_jobs))
    f_ = pd.concat(f_, axis=0, ignore_index=True)
    p.close()
    p.join()
    return f_.values
