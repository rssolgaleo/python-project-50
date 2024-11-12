from gendiff.formatters.stylish import default_formatter


def diff_formatter(diff, format):
    if format == 'stylish':
        return default_formatter(diff)
