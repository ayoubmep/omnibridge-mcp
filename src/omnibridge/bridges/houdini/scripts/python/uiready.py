# Runs once Houdini's interface is ready (interactive sessions only).
try:
    import omnibridge_houdini

    omnibridge_houdini.start()
except Exception as error:  # never block Houdini's startup
    print("OmniBridge did not start: %s" % error)
