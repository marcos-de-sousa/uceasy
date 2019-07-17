import subprocess
from uceasy.adapters import CPU, PHYLUCE


class UCEProcessor:
    def __init__(self, output):
        self.__output = output

    def match_contigs_to_probes(self, contigs, probes):
        return [
            PHYLUCE + '/bin/phyluce_assembly_match_contigs_to_probes',
            '--contigs', contigs,
            '--probes', probes,
            '--output', self.__output
        ]

    def get_match_counts(self, locus_db, taxon_list_config, taxon_group):
        return [
            PHYLUCE + '/bin/phyluce_assembly_get_match_counts',
            '--locus-db', locus_db,
            '--taxon-list-config', taxon_list_config,
            '--taxon-group', taxon_group,
            '--output', self.__output
        ]

    def get_fastas_from_match_counts(self, contigs, locus_db, match_count_output, log_path):
        return [
            PHYLUCE + '/bin/phyluce_assembly_get_fastas_from_match_counts',
            '--contigs', contigs,
            '--locus-db', locus_db,
            '--match-count-output', match_count_output,
            '--output', self.__output,
            '--log-path', log_path
        ]

    def explode_get_fastas_file(self, alignments):
        return [
            PHYLUCE + '/bin/phyluce_assembly_explode_get_fastas_file',
            '--alignments', alignments,
            '--output', self.__output,
            '--by-taxon'
        ]

    def seqcap_align(self, fasta, taxa, aligner, no_trim=False):
        return [
            PHYLUCE + '/bin/phyluce_align_seqcap_align',
            '--fasta', fasta,
            '--taxa', taxa,
            '--aligner', aligner,
            '--output', self.__output
        ]
        if no_trim:
            cmd.append('--no-trim')

    def get_gblocks_trimmed_alignments_from_untrimmed(self, alignments, log):
        return [
            PHYLUCE + '/bin/get_gblocks_trimmed_alignments_from_untrimmed',
            '--alignments', alignments,
            '--output', self.__output,
            '--log', log
            ]

    def remove_locus_name_from_nexus_lines(self, alignments, log):
        return [
            PHYLUCE + '/bin/remove_locus_name_from_nexus_lines',
            '--alignments', alignments,
            '--output', self.__output,
            '--log-path', log,
            '--cores', CPU
        ]

    def get_only_loci_with_min_taxa(self, alignments, taxa, percent, log):
        return [
            PHYLUCE + '/bin/get_only_loci_with_min_taxa',
            '--alignments', alignments,
            '--taxa', taxa,
            '--percent', percent,
            '--output', self.__output,
            '--cores', CPU,
            '--log-path', log
        ]

    def format_nexus_files_for_raxml(self, alignments, log, charsets=False):
        cmd = [
            PHYLUCE + '/bin/format_nexus_files_for_raxml',
            '--alignments', alignments,
            '--output', self.__output,
            '--log-path', log
        ]
        if charsets:
            cmd.append('--charsets')
        return cmd

