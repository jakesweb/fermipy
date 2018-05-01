# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import absolute_import, division, print_function

from fermipy.tests.utils import requires_dependency

try:
    from fermipy.jobs.gtlink import Gtlink
    from fermipy.jobs.file_archive import FileFlags
except ImportError:
    pass

# Skip tests in this file if Fermi ST aren't available
pytestmark = requires_dependency('Fermi ST')




def test_gtlink():

    class Gtlink_scrmaps(Gtlink):
        appname= 'gtsrcmaps'
        linkname_default = 'gtsrcmaps'
        usage = '%s [options]' %(appname)
        description = "Link to run %s"%(appname)
        
        default_options=dict(irfs=('CALDB', 'options', str),
                             expcube=(None, 'Input exposure hypercube', str),
                             bexpmap=(None, 'Input binnned exposure map', str),
                             cmap=(None, 'Input counts map', str),
                             srcmdl=(None, 'Input source model', str),
                             outfile=(None, 'Output file', str))
    
        default_file_args=dict(expcube=FileFlags.input_mask,
                               cmap=FileFlags.input_mask,
                               bexpmap=FileFlags.input_mask,
                               srcmdl=FileFlags.input_mask,
                               outfile=FileFlags.output_mask)

        def __init__(self, **kwargs):
            """C'tor
            """
            linkname, init_dict = self._init_dict(**kwargs)
            super(Gtlink_scrmaps, self).__init__(linkname, **init_dict)


    gtlink = Gtlink_scrmaps()
    formatted_command = gtlink.formatted_command()
    assert formatted_command == 'gtsrcmaps irfs=CALDB expcube=None cmap=None srcmdl=None outfile=None bexpmap=None'


if __name__ == '__main__':
    gtlink = test_gtlink()
