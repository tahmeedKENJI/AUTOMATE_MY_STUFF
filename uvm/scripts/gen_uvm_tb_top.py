import sys
import os

if len(sys.argv) < 1:
    sys.exit(1)

file_path = sys.argv[1]

os.makedirs(os.path.dirname(file_path), exist_ok=True)

content = f"""\
`include "dependencies.svh"

module uvm_tb_top;

    logic clk, rst_n;

    task automatic start_clk(int clk_freq_MHz);
        real time_period;
        time_period = 1000 / clk_freq_MHz;
        fork
            forever begin
                clk <= '0;
                #(time_period / 2);
                clk <= '1;
                #(time_period / 2);
            end
        join_none
    endtask

    initial begin
        string testname;
        int clk_freq_MHz;
        
        string def_testname;
        int def_clk_freq_MHz;

        if (!$value$plusargs("TESTNAME=%s", testname)) testname = def_testname;
        if (!$value$plusargs("CLKFREQMHZ=%d", clk_freq_MHz)) clk_freq_MHz = def_clk_freq_MHz;
        `uvm_info("TOP", $sformatf("\nSYS_CLK: %0d MHz\nTEST_NAME: %s\n", clk_freq_MHz, testname), UVM_HIGH)

        // uvm_config_db #()::set(null, "*", " ", );

        start_clk(clk_freq_MHz); // Specify Clock Speed

        run_test(testname);
    end

endmodule
"""

with open(file_path, "w") as f:
    f.write(content)