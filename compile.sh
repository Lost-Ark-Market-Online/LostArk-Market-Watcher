
ARGS=$(getopt -a --options dr --long "debug,release" -- "$@")
eval set -- "$ARGS"

release="false"
debug="false"

while true; do
  case "$1" in
    -r|--release)
      release="true"
      shift;;
    -d|--debug)
      debug="true"
      shift;;
    --)
      break;;
     *)
      printf "Unknown option %s\n" "$1"
      exit 1;;
  esac
done

if [[ $release == true ]]; then
  pyinstaller release.spec
elif [[ $debug == true ]]; then
  pyinstaller debug.spec
fi