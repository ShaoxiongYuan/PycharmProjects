class IterableHelper:
    @staticmethod
    def find_single(iterable, func):
        for item in iterable:
            if func(item):
                return item.__dict__

    @staticmethod
    def find_all(iterable, func):
        for item in iterable:
            if func(item):
                yield item.__dict__

    @staticmethod
    def find_all_no_condition(iterable, func_handle):
        for item in iterable:
            yield func_handle(item)

    @staticmethod
    def find_maximum(iterable, func):
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            if func(max_value) < func(iterable[i]):
                max_value = iterable[i]
        return max_value.__dict__

    @staticmethod
    def sort(iterable, func):
        for i in range(len(iterable) - 1):
            for item in range(i + 1, len(iterable)):
                if func(iterable[i]) > func(iterable[item]):
                    iterable[i], iterable[item] = iterable[item], iterable[i]
