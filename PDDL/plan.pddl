POPF, Release 2
By releasing this code we imply no warranty as to its reliability
and its use is entirely at your own risk.

Usage: /home/enzo/Scrivania/ROS_RT2/ros_ws/src/ROSPlan/rosplan_planning_system/common/bin/popf [OPTIONS] domainfile problemfile [planfile, if -r specified]

Options are: 

	-citation	Display citation to relevant conference paper (ICAPS 2010);
	-b		Disable best-first search - if EHC fails, abort;
	-E		Skip EHC: go straight to best-first search;
	-e		Use standard EHC instead of steepest descent;
	-h		Disable helpful-action pruning;
	-k		Disable compression-safe action detection;
	-c		Disable the tie-breaking in RPG that favour actions that slot into the partial order earlier;
	-S		Sort initial layer facts in RPG by availability order (only use if using -c);
	-m		Disable the tie-breaking in search that favours plans with shorter makespans;
	-F		Full FF helpful actions (rather than just those in the RP applicable in the current state);
	-r		Read in a plan instead of planning;
	-T		Rather than building a partial order, build a total-order
	-n		Optimise, finding many solutions;
	-v<n>		Verbose to degree n (n defaults to 1 if not specified).
	-L<n>		LP verbose to degree n (n defaults to 1 if not specified).
