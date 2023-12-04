import * as React from 'react';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import ListSubheader from '@mui/material/ListSubheader';
import BarChart from '@mui/icons-material/BarChart';
import CandlestickChartIcon from '@mui/icons-material/CandlestickChart';

type MainListItemsProps = {
  activeTab: string,
  onClickHandler: Function
}

export default function MainListItems({ activeTab, onClickHandler = () => {} }: MainListItemsProps) {
    return (
      <React.Fragment>
        <ListSubheader component="div" inset>
          Starship Trends
        </ListSubheader>
        <ListItemButton selected={activeTab === 'lineChart'} onClick={() => {onClickHandler('lineChart')}}>
          <ListItemIcon>
            <BarChart />
          </ListItemIcon>
          <ListItemText primary="Line Chart" />
        </ListItemButton>
        <ListItemButton selected={activeTab === 'boxBlot'} onClick={() => {onClickHandler('boxPlot')}}>
          <ListItemIcon>
            <CandlestickChartIcon />
          </ListItemIcon>
          <ListItemText primary="Box Plot" />
        </ListItemButton>
      </React.Fragment>
    )
}