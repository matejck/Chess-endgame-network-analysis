```{=latex}
\begin{table}[ht!]
\centering
\caption{Comparison of the top 5 communities ranked by individual community quality ($\mathcal{Q}_{0.5}^\textnormal{norm}$) and safest reachable targets by path cost ($\mathcal{C}_{0.5}$) for depth 7.}
\begin{tabular}{c l l}
\hline
\textbf{Rank} & \textbf{Best $\mathcal{Q}_{0.5}^\textnormal{norm}$ Scores} & \textbf{Lowest Path Cost ($\mathcal{C}_{0.5}$)} \\
\hline
$1$ & $0.911$ (Community 19) & $0.000$ (Community 6) \\
$2$ & $0.890$ (Community 21) & $0.164$ (Community 7) \\
$3$ & $0.870$ (Community 22) & $0.204$ (Community 11) \\
$4$ & $0.849$ (Community 7) & $0.257$ (Community 19) \\
$5$ & $0.816$ (Community 11) & $0.280$ (Community 21) \\
\hline
\end{tabular}
\label{table.network2.scores}
\end{table}
```

```{=latex}
\begin{table}[ht!]
\centering
\caption{Preservation of community structure at depth 7 measured by average Normalized Mutual Information (NMI) across probabilities.}
\begin{tabular}{c c c}
\hline
\textbf{Probability ($p$)} & \textbf{Node Sampling NMI} & \textbf{DFS Sampling NMI} \\
\hline
$0.9$ & $0.967$ \raisebox{0.1ex}{\scriptsize $\pm 0.011$} & $0.941$ \raisebox{0.1ex}{\scriptsize $\pm 0.012$} \\
$0.8$ & $0.964$ \raisebox{0.1ex}{\scriptsize $\pm 0.011$} & $0.898$ \raisebox{0.1ex}{\scriptsize $\pm 0.013$} \\
$0.7$ & $0.956$ \raisebox{0.1ex}{\scriptsize $\pm 0.014$} & $0.841$ \raisebox{0.1ex}{\scriptsize $\pm 0.010$} \\
$0.6$ & $0.946$ \raisebox{0.1ex}{\scriptsize $\pm 0.015$} & $0.777$ \raisebox{0.1ex}{\scriptsize $\pm 0.010$} \\
$0.5$ & $0.934$ \raisebox{0.1ex}{\scriptsize $\pm 0.014$} & $0.692$ \raisebox{0.1ex}{\scriptsize $\pm 0.012$} \\
$0.4$ & $0.903$ \raisebox{0.1ex}{\scriptsize $\pm 0.017$} & $0.584$ \raisebox{0.1ex}{\scriptsize $\pm 0.009$} \\
$0.3$ & $0.837$ \raisebox{0.1ex}{\scriptsize $\pm 0.016$} & $0.459$ \raisebox{0.1ex}{\scriptsize $\pm 0.008$} \\
$0.2$ & $0.721$ \raisebox{0.1ex}{\scriptsize $\pm 0.021$} & $0.463$ \raisebox{0.1ex}{\scriptsize $\pm 0.103$} \\
$0.1$ & $0.677$ \raisebox{0.1ex}{\scriptsize $\pm 0.017$} & $0.426$ \raisebox{0.1ex}{\scriptsize $\pm 0.197$} \\
\hline
\end{tabular}
\label{table.network2.NMI}
\end{table}
```