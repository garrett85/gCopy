import Args
import sweep
import init

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init.init()

    args = Args.getArgs()
    sourceList = dict(sweep.sweep(args['source']))
    targetList = dict(sweep.sweep(args['target']))

    # I need to do the following inside sweep to take advantage of yeild for resource consumstion
    for i in sourceList:
        if i not in targetList:
            print(i, sourceList[i])

    # for i in targetList:
    #     print(i)

    # comparison = {}
    # for hashedSource, sourcePath in sourceList:
    #     for hashedTarget, targetPath in targetList:

    # if args['']

    # for option, value in args.items():
    #     print(f"{option}: {value}")
