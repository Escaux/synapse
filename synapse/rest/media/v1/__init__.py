#
# This file is licensed under the Affero General Public License (AGPL) version 3.
#
# Copyright 2014-2016 OpenMarket Ltd
# Copyright (C) 2023 New Vector, Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# See the GNU Affero General Public License for more details:
# <https://www.gnu.org/licenses/agpl-3.0.html>.
#
# Originally licensed under the Apache License, Version 2.0:
# <http://www.apache.org/licenses/LICENSE-2.0>.
#
# [This file includes modifications made by New Vector Limited]
#
#

from PIL.features import check_codec

# check for JPEG support.
if not check_codec("jpg"):
    raise Exception(
        "FATAL: jpeg codec not supported. Install pillow correctly! "
        " 'sudo apt-get install libjpeg-dev' then 'pip uninstall pillow &&"
        " pip install pillow --user'"
    )


# check for PNG support.
if not check_codec("zlib"):
    raise Exception(
        "FATAL: zip codec not supported. Install pillow correctly! "
        " 'sudo apt-get install libjpeg-dev' then 'pip uninstall pillow &&"
        " pip install pillow --user'"
    )
