# Copyleft 2018 - 12c
# License: GPLv3 (see http://www.gnu.org/licenses/gpl.html)

import markup
import info_table
import os.path
import subprocess


LABEL = u"Placas de Red"


class Info(object):

    @staticmethod
    def text():
        cmd= ['lspci | grep -E "Network | network | Ethernet | ethernet | wireless | Wireless" | cut -c9-100']
        process = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE)
        out, err = process.communicate()
        info = out.strip()
        info = '\n' + info
        return info

    @staticmethod
    def label():
        return LABEL


if __name__ == '__main__':
    #print '{0}: {1}'.format(Info.label(), Info.text())
    null

else:
    info_table.add_row_to_table(markup.label_set_markup(Info.label()), markup.text_set_markup(Info.text()), 10, "Placas de Red")
