# Instructions

1. Copy the .mk file into your directory and rename it "Makefile"
2. Copy the scripts folder into your directory
3. use the following commands:

| command            | Parameters        | Result                               |
|--------------------|-------------------|--------------------------------------|
| make init          |                   | Initializes the directory |
| make deinit        |                   | Nukes the directory |
| make uvm_test_init | TESTNAME | Creates a testcase specified by TESTNAME |
| make uvm_component_init | COMPONENT | Creates a set of uvm components with prefix specified by COMPONENT | 
| make uvm_seq_item_init | SEQ_ITEM | Creates a new sequence item specified by SEQ_ITEM |
| make uvm_sequence_init | SEQUENCE | Creates a new sequence specified by SEQUENCE |
| make uvm_inheritor_init | TESTNAME, INHERITOR | Creates a new inheritor specified by INHERITOR extending from the test specified by TESTNAME |
| make uvm_object_init | OBJECT | Creates a new sequence specified by OBJECT |
| make flist | | Generate file list for simulation. Re-order manually the files to control the compilation order |
| make run_sim | TESTTYPE, TESTNAME | Run test simulation specified by TESTNAME. Use TESTTYPE=TB for SV TB, TESTTYPE=UVM for UVM TB |
| make run_gui | TESTTYPE, TESTNAME | Run test simulation specified by TESTNAME on GUI. Use TESTTYPE=TB for SV TB, TESTTYPE=UVM for UVM TB |
| make clean | | Cleans up the generated residue simulation files |   