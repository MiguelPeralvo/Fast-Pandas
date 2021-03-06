from Benchmarker import Benchmarker


def regular(df):
    df["E"] = df["A"] * df["B"] + df["C"]


def eval_method(df):
    df.eval("E = A * B + C", inplace=True)


params = {
    "df_generator": 'pd.DataFrame(np.random.randint(1, df_size, (df_size, 4)), columns=list("ABCD"))',
    "functions_to_evaluate": [regular, eval_method],
    "title": "Benchmark for column creation",
}

benchmark = Benchmarker(**params)
benchmark.benchmark_all()
benchmark.print_results()
benchmark.plot_results()
